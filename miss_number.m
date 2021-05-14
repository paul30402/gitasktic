while true
	try %try...catch...end: https://www.itread01.com/content/1541827408.html
    %try...catch...end用法：https://blog.csdn.net/Intangilble/article/details/83411025
        iter_str = input('Take in numbers: ', 's');
        %Request user input: https://www.mathworks.com/help/matlab/ref/input.html
        iter_str = split(iter_str);
        %split: https://www.mathworks.com/help/matlab/ref/split.html
        iter_int = str2double(iter_str);
        %Convert Cell Array to Num array: https://www.mathworks.com/matlabcentral/answers/15232-convert-cell-array-to-num-array
        for i=iter_int
            i;
            if sum(isnan(i)) > 0
                %Find NaN elements in a matrix: https://www.mathworks.com/matlabcentral/answers/18150-find-nan-elements-in-a-matrix
                errorStruct.message = 'Data file not found. test';
                %errorStruct.identifier = 'MyFunction:fileNotFound';  
                error(errorStruct)
                %raise error: https://www.mathworks.com/help/matlab/ref/error.html
            end
        end
        disp(['A series of numbers you typed was:' num2str(iter_int')]);
    catch err
        %如果E運行錯誤
        %執行catch和end之間的程式碼
        fprintf('Wrongly type, please type integers only！');
        continue
        %How do I force the next loop iteration if error occurs within the loop?
        %https://www.mathworks.com/matlabcentral/answers/224369-how-do-i-force-the-next-loop-iteration-if-error-occurs-within-the-loop
    end
    %Step 1: setting up your repository with a python file.
    %(1)Write a python function that find a missing number in a list
    list_A = [min(iter_int): max(iter_int)];
    miss=setdiff(list_A, iter_int);

    if length(miss) == 1
        %求向量長度: https://zhidao.baidu.com/question/142230855363077885.html?qbl=relate_question_0
        disp(['There is one missing number: ' num2str(miss)])
        break
    elseif length(miss) > 1
        disp(['There are multiple missing numbers: ' num2str(miss)])
        break
    elseif length(miss) == 0
        disp('There is no missing number.')    
        break
    end
end



